/*
collection of known errorcodes
b2500-v2 ( fw 216+ )
*/

std::map<int, std::string> errorMap2 = {
	{ 0, "Device startup" },
	{ 12, "Battery Overvoltage" },
	{ 25, "Watchdog reset" },
	{ 33, "Lithium short circuit protection" },
	{ 35, "Single battery overvoltage" },
	{ 36, "Single section undervoltage" },
	{ 42, "Register notification undervoltage" },
	{ 43, "Under voltage condition enters sleep mode" },
	{ 51, "BMS charging low-temperature protection" },
	{ 55, "Start discharge learning" },
	{ 56, "Start charging and learning" },
	{ 57, "Interrupted discharge learning" },
	{ 60, "Discharge learning completed" },
	{ 61, "Charging learning completed" },
	{ 62, "Invalid learning data" },
	{ 63, "Discharge opens and exits charging learning" },
	{ 64, "Enter warehouse transportation mode" },
	{ 65, "Wake up in warehouse transportation mode" },
	{ 74, "MQTT open failed" },
	{ 75, "MQTT connection disconnected" },
	{ 76, "MQTT Reconnect" },
	{ 77, "DOD stops discharging" },
	{ 78, "MQTT connection successful" },
	{ 79, "Bind monitor IP" },
	{ 80, "MQTT re upload" },
	{ 81, "MQTT certificate deletion" },
	{ 82, "MQTT upload successful" },
	{ 84, "HTTPGET error" },
	{ 85, "Output 2 abnormal" },
	{ 86, "MQTT re upload" },
	{ 87, "MQTT delete certificate" },
	{ 88, "MQTT upload successful" },
	{ 89, "Output 1 channel abnormal" },
	{ 90, "Output 2 channels abnormal" },
	{ 91, "HTTPPOST error" },
	{ 92, "Battery pack DOD parking" },
	{ 93, "Battery pack switching" },
	{ 94, "Abnormal low-power output" },
	{ 95, "Abnormal battery pack switching" },
	{ 100, "risk of backflow" },
	{ 255, "end of list" }
};

