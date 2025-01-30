const int LED_PIN = 1;  // PB1 (Physical Pin 6)

void setup() {
    cli();  // Disable interrupts (prevents bootloader weirdness)
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    // Set unused pins as outputs to prevent floating
    pinMode(0, OUTPUT); digitalWrite(0, LOW);
    pinMode(2, OUTPUT); digitalWrite(2, LOW);
    pinMode(3, OUTPUT); digitalWrite(3, LOW);
    pinMode(4, OUTPUT); digitalWrite(4, LOW);

    // Enable pull-ups on any inputs
    pinMode(2, INPUT_PULLUP);
    pinMode(3, INPUT_PULLUP);

    sei();  // Enable interrupts

    delay(5000);  // Let bootloader finish
}

void loop() {
    digitalWrite(LED_PIN, HIGH);
    delay(1000);
    digitalWrite(LED_PIN, LOW);
    delay(1000);
}
