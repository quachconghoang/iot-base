#include <cstdio>
#include <cstring>

#include "temperature_conversion.h"
#include <mosquittopp.h>

mqtt_tempconv::mqtt_tempconv(const char *id, const char *host, int port) : mosquittopp(id)
{
    int keepalive = 60;

    /* Connect immediately. This could also be done by calling
     * mqtt_tempconv->connect(). */
//    username_pw_set("admin", "admin");
    topicName=std::string(id);
    connect(host, port, keepalive);
};

mqtt_tempconv::~mqtt_tempconv()
{
}

void mqtt_tempconv::on_connect(int rc)
{
    printf("Connected with code %d.\n", rc);
    if(rc == 0){
        /* Only attempt to subscribe on a successful connect. */
        subscribe(NULL, topicName.c_str());
    }
}

void mqtt_tempconv::on_message(const struct mosquitto_message *message)
{
    double temp_celsius, temp_farenheit;
    char buf[51];

    if(!strcmp(message->topic, topicName.c_str())){
//        memset(buf, 0, 51*sizeof(char));
//        /* Copy N-1 bytes to ensure always 0 terminated. */
//        memcpy(buf, message->payload, 50*sizeof(char));
//        temp_celsius = atof(buf);
//        temp_farenheit = temp_celsius*9.0/5.0 + 32.0;
//        snprintf(buf, 50, "%f", temp_farenheit);
//        snprintf(buf, 50, "%f", temp_celsius);
        printf("%s \n", message->payload);
//        publish(NULL, "temperature/farenheit", strlen(buf), buf);
    }
}

void mqtt_tempconv::on_subscribe(int mid, int qos_count, const int *granted_qos)
{
    printf("Subscription succeeded.\n");
}
