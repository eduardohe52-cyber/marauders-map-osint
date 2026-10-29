#include <WiFi.h>
#include <esp_wifi.h>

// Configuración de red para enviar los datos al servidor (MQTT)
const char* ssid = "TU_WIFI_SSID";
const char* password = "TU_WIFI_PASSWORD";

// Callback que se ejecuta cada vez que el ESP32 "escucha" un paquete Wi-Fi
void sniffer(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t *)buf;
    
    // Si es un paquete de gestión (como un Probe Request)
    if (type == WIFI_PKT_MGMT) {
        // Aquí extraeríamos la MAC y el RSSI (simplificado para el ejemplo)
        int rssi = pkt->rx_ctrl.rssi;
        Serial.print("Paquete detectado. RSSI: ");
        Serial.println(rssi);
        
        // En un código real, aquí enviarías el RSSI y la MAC por MQTT al servidor Python
    }
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    
    // Ponemos la tarjeta en modo monitor/promiscuo
    esp_wifi_set_promiscuous(true);
    esp_wifi_set_promiscuous_rx_cb(&sniffer);
    Serial.println("ESP32 en modo Monitor. Escuchando...");
}

void loop() {
    // El trabajo se hace en el callback (sniffer), así que el loop puede estar vacío
    delay(1000);
}
