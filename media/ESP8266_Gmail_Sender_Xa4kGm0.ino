#include <ESP8266WiFi.h>
#include <ESP8266SMTP.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>


//Данные для режима обновления
const char* hostWeb = "esp8266-webupdate";
const char* ssidWeb = "SM-00001";
const char* passwordWeb = "1234567890";
ESP8266WebServer server(80);
const char* serverIndex = "<form method='POST' action='/update' enctype='multipart/form-data'><input type='file' name='update'><input type='submit' value='Update'></form>";



//Данные для ражима работы или сна
String sensor_id = "SM-00001"; //Уникальный номер устройства SM - soil moisture
const char* ssid = "TP-Link_NEW";                // WIFI network name
const char* password = "121119995";            // WIFI network password
//const char *ssid = "Mark";
//const char *password = "1234567890";

uint8_t connection_state = 0;           // Connected to WIFI or not
uint16_t reconnect_interval = 10000;    // If not connected wait time to try again

int time_resend=6;//Время в часах сна, если не удалось подключиться или отправить данные

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");


//////////////////////////////////////////////////////
//Подключение к WIFI
//////////////////////////////////////////////////////
uint8_t WiFiConnect(const char* ssID, const char* nPassword)
{
  static uint16_t attempt = 0;
  Serial.print("Connecting to ");
  Serial.println(ssID);
  WiFi.begin(ssID, nPassword);

  uint8_t i = 0;
  while(WiFi.status() != WL_CONNECTED && i++ < 50) {
    delay(200);
    Serial.print(".");
  }
  ++attempt;
  Serial.println("");
  if(i == 51) {
    Serial.print(F("Connection: TIMEOUT on attempt: "));
    Serial.println(attempt);
    if(attempt % 2 == 0)
      Serial.println(F("Check if access point available or SSID and Password are correct\r\n"));
    return false;
  }
  Serial.println(F("Connection: ESTABLISHED"));
  Serial.print(F("Got IP address: "));
  Serial.println(WiFi.localIP());
  return true;
}


///////////////////////////////////////////////////////////////
//Сон
///////////////////////////////////////////////////////////////
void deepSleepCycle(bool end_of_setup = false) {

    uint32_t reset_counter = 0;
    bool waking_from_sleep = ESP.getResetReason() == "Deep-Sleep Wake";

    if (!end_of_setup) {
        if (waking_from_sleep) {
            Serial.print("Waking up from deep-sleep via reset pin. Reset counter: ");
            ESP.rtcUserMemoryRead(0, &reset_counter, sizeof(reset_counter));
            reset_counter++;
            ESP.rtcUserMemoryWrite(0, &reset_counter, sizeof(reset_counter));
            Serial.println(String(reset_counter));
        } else {
            Serial.println("Zeroing reset counter.");
            ESP.rtcUserMemoryWrite(0, &reset_counter, sizeof(reset_counter));
            return;
        }
    }
    
    uint32_t hours = 0;
    ESP.rtcUserMemoryRead(1, &hours, sizeof(hours));
    
    // With larger values, deep-sleep is unrealiable: it might never wake up and consume a lot of power.
    // Therefore sleep one hour at a time.
    // In reality, the ESP sleeps a bit less than the 60 minutes it is told to.
    if (reset_counter < hours) {
        // If this is the first time going to sleep, do the radio calibration once.
        // Otherwise, disable radio (WiFi).
        RFMode wake_mode = waking_from_sleep ? WAKE_RF_DISABLED : WAKE_RFCAL;
        if (reset_counter + 1 == hours) {
            // Wake up with radio on if the next power cycle finishes sleeping.
            wake_mode = WAKE_NO_RFCAL;
        }
        Serial.println("Going to deep-sleep for 1 hour.");
        // 1: WAKE_RFCAL
        // 2: WAKE_NO_RFCAL
        // 4: WAKE_RF_DISABLED
        Serial.print("sleep: ");
        Serial.println(hours-reset_counter);
        Serial.println("Radio mode will be: " + String(wake_mode));
        ESP.deepSleep(3600*1e6, wake_mode);
    }
    reset_counter = 0;
    ESP.rtcUserMemoryWrite(0, &reset_counter, sizeof(reset_counter));

}


void setup()
{
  //Serial.begin(115200);
  Serial.begin(74880);
  delay(2000);

  pinMode(12, INPUT);
  int do_sleep = digitalRead(12);
  Serial.println(do_sleep);
  if(do_sleep==1){//Кнопка нажата, переходим к настройкам или обновлению
    pinMode(13, OUTPUT);
    delay(100);
    digitalWrite(13, HIGH);
    updateMake();
  }else{//Спим или просыпаемся для действия
    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);
    sleepMake();
  }
  
}


//Спим или просыпаемся для действия
void sleepMake(){
  uint32_t hours=time_resend;//Предустанавливаем время если не удалось подключиться
  deepSleepCycle();

  connection_state = WiFiConnect(ssid, password);
  
  if(connection_state) {// if not connected to WIFI
    //Получаем время сколько еще спать
//    timeClient.begin();
//    timeClient.setTimeOffset(14400);
//    timeClient.update();
//    int currentHour = timeClient.getHours();
//    if(currentHour>=12){//Больше 12 часов
//      hours = 24 - currentHour;
//      if(hours<3){
//        hours=hours+12;
//      }
//    }else{//Меньше
//      hours = 12 - currentHour;
//      if(hours<3){
//        hours=hours+12;
//      }
//    }

    //Делаем замер
    pinMode(14, OUTPUT);
    delay(100);
    digitalWrite(14, HIGH);
    delay(100);
    String str="{ 'id':";
    str+="'"+sensor_id+"', ";
    str+="'hum':";

    int minBorderHum=700;//Нижняя граница данных
    int aRead=analogRead(A0);
    int percent = map(aRead, 230, 550, 100, 0);
    str+=percent;
    str+=" }";
    
    Serial.println(str);    
    digitalWrite(14, LOW);

    //Отправляем сообщение
    SMTP.setEmail("vsevodat001@gmail.com")
      .setPassword("qazcderfvxswedc123")
      .Subject("Now Time Send")
      .setFrom("vsevodat001@gmail.com")
      .setForGmail();
    
    if(SMTP.Send("vsevotel1@gmail.com", str)) {
      Serial.println(F("Message sent"));
    } else {
      Serial.print(F("Error sending message: "));
      Serial.println(SMTP.getError());
      hours=time_resend;
    } 
  }

  //Обновляем время сна и спим
  ESP.rtcUserMemoryWrite(1, &hours, sizeof(hours));
  Serial.print("all sleep: ");
  Serial.println(hours);
  deepSleepCycle(true);
}

void updateMake(){

  Serial.print("Setting soft-AP ... "); //  "Настройка программной точки доступа ... "
  boolean result = WiFi.softAP(ssidWeb, passwordWeb);
  if(result == true)
  {
    Serial.println("Ready");//  "Готово"
    
    Serial.println(WiFi.softAPIP());
    server.on("/", HTTP_GET, []() {
      server.sendHeader("Connection", "close");
      server.send(200, "text/html", serverIndex);
    });
    
    server.on("/datas", HTTP_GET, []() {
      String st1 = "";
      st1+= analogRead(A0);
      pinMode(14, OUTPUT);
      delay(100);
      digitalWrite(14, HIGH);
      delay(1000);
      String st2 = "";
      st2+= analogRead(A0);
      digitalWrite(14, LOW);
      server.send(200, "text/html", st1+" "+st2);
    });
    
    server.on("/update", HTTP_POST, []() {
      server.sendHeader("Connection", "close");
      server.send(200, "text/plain", (Update.hasError()) ? "FAIL" : "OK");
      ESP.restart();
    }, []() {
      HTTPUpload& upload = server.upload();
      if (upload.status == UPLOAD_FILE_START) {
        Serial.setDebugOutput(true);
        WiFiUDP::stopAll();
        Serial.printf("Update: %s\n", upload.filename.c_str());
        uint32_t maxSketchSpace = (ESP.getFreeSketchSpace() - 0x1000) & 0xFFFFF000;
        if (!Update.begin(maxSketchSpace)) { //start with max available size
          Update.printError(Serial);
        }
      } else if (upload.status == UPLOAD_FILE_WRITE) {
        if (Update.write(upload.buf, upload.currentSize) != upload.currentSize) {
          Update.printError(Serial);
        }
      } else if (upload.status == UPLOAD_FILE_END) {
        if (Update.end(true)) { //true to set the size to the current progress
          Serial.printf("Update Success: %u\nRebooting...\n", upload.totalSize);
        } else {
          Update.printError(Serial);
        }
        Serial.setDebugOutput(false);
      }
      yield();
    });
    server.begin();
  }
  else
  {
    Serial.println("Failed!");//  "Настроить точку доступа не удалось"
  }


}

void loop(){
  server.handleClient();
 }
