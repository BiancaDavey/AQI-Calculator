#!/usr/bin/env python3

# This function calculates and returns Air Quality Index (AQI) reading(s).

def air_quality():

  # x represents total number of readings to be calculated, set by user input.
  # y serves as a counter for the reading number currently being calculated by the function.

  # Initial loop prompts user input to set number of readings to be calculated.
  #
  # User input must be a positive integer value.
  # Function restarts if user does not enter a positive integer.
  # Function continues once user inputs a positive integer.

  try:
    x = int(input("Enter number of readings: "))
  except ValueError:
    print("Please enter a positive number.")
    air_quality()
  else:
    if x <= 0:
      print ("Please enter a positive number.")
      air_quality()
    else:
      y = 1  # y is initialised as 1 to begin reading count.

      # Outermost while loop re-runs for each reading  until total number of readings specified by
      # user are returned.

      while x > 0:
        print("Reading", y)  # Displays read number currently being calculated.

        # Interior while loops prompt user input for pollutant levels recorded for ozone,
        # sulfur dioxide, and particles less than 2.5 micrometres in diameter.
        #
        # User input must be a positive integer or floating point value.
        # Loop restarts if user does not enter a positive integer or floating point value.
        # Next loop runs once user inputs a positive integer or floating point.

        while True:
          try:
            ozone = float(input("Amount of ozone recorded (parts per hundred million): "))
            if ozone < 0:
              raise(ValueError)
            break
          except ValueError:
            print("Please enter a nonnegative number.")
        while True:
          try:
            sulfur_dioxide = float(input("Amount of sulfur dioxide recorded (parts per hundred million): "))
            if sulfur_dioxide < 0:
              raise(ValueError)
            break
          except ValueError:
            print("Please enter a positive number.")
        while True:
          try:
            particles = float(input("Amount of particles less than 2.5 micrometres diameter (micrograms per cubic metre): "))
            if particles < 0:
              raise(ValueError)
            break
          except ValueError:
            print("Please enter a positive number.")

        # AQI is calculated for each pollutant separately, based on the level recorded and input by
        # the user, divided by the standard level of that pollutant, and multiplied by one hundred.
        # The final AQI reading is the highest of the readings calculated for each pollutant.

        ozone_AQI = 100*(ozone/8)
        sulfur_dioxide_AQI = 100*(sulfur_dioxide/20)
        particles_AQI = 100*(particles/25)
        AQI = [ozone_AQI, sulfur_dioxide_AQI, particles_AQI]
        AQI_pollutant = max(AQI)  # max is used to provide the highest of the pollutant readings.

        # The final AQI reading is displayed.
        # The total number of readings to be calculated is decremented by 1. This will re-run the
        # outermost while loop until the countdown reaches zero.
        # The reading number for display purposes is incremented by 1 for the next reading(s) (if any).

        print("AQI is", AQI_pollutant)
        x = x-1
        y = y+1


# Function call

air_quality()
