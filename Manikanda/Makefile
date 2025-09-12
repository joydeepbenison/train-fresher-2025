# Name of the executable
TARGET = cal

# Compiler to use
CC = gcc

# Compiler flags
CFLAGS = -Wall -g

# Default rule (build the program)
$(TARGET): cal.c
	$(CC) $(CFLAGS) -o $(TARGET) cal.c

# Clean rule (remove compiled files)
clean:
	rm -f $(TARGET)
