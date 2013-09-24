#!/usr/bin/python

# Mullis GCode Creator 
# Version 1.3 
# By: Andrew Selzer
# Copyleft 2012
#
# Changes: Added ability to write G-Code without comments. v1.1
# Changes: Added ability to adjust motor speed. v1.2.
# Changes: Added ability to adjust tray adjustment unit length. Removed unnessary comments. v1.3.
#

print "Welcome to Mullis GCode creator Version 1.3!\n";

# Ask User For Tray Unit Length
tray_query = raw_input ("Would would like the length the tray is loaded adjusted? (Please input yes or no)\n");

if tray_query in ('yes', 'YES', 'Yes', 'y', 'Y'):
        tray_value = raw_input ("\nPlease input unit length value: \n");
        print "\nYou have selected "+tray_value+" as your unit length value. \n";

else: 
        tray_value = 2500
        print "\nThe default unit length value of 2500 will be used. \n";

# Ask User For Feedrate
feedrate_query = raw_input ("Would you like the motor speed adjusted? (Please input yes or no)\n");

if feedrate_query in ('yes', 'YES', 'Yes', 'y', 'Y'):
        feedrate =  raw_input ("\nPlease input motor speed value: \n");
        print "\nYou have selected "+feedrate+" as your motor speed. \n";
else: 
        feedrate = 50000
        print "\nThe default motor speed of 50000 will be used. \n";

# Ask User For Comments
comments = raw_input( "Would you like your code with comments? (Please input yes or no)\n");

# Opens a File
fo = open("mullis.gcode", "wb")

if comments in ('yes','YES','Yes','y','Y'):
        # Print Statement for Comments Enabled
        print "\nThis GCode will be generated with Comments Enabled.\n";

        # Writes G-Code to File
        fo.write("M28 X18 ; home x axis\n\n")
        fo.write("G91 ; use relative positioning\n\n")
        fo.write("G1 X10 F2200 ; these three lines are the header\n\n")
        fo.write("G1 F"+str(feedrate)+" ; this is the speed of the motor, adjust it to make the extruder go faster or slower \n\n")
        fo.write("G1 E"+str(tray_value)+" ; Lower tray for a length of units. To go farther, adjust the number after the E (extrude).\n\n")
        fo.write("G4 P30000 ; this is the pause command. P is the time paused in milliseconds.\n\n")
        fo.write("G1 F"+str(feedrate)+"\n\n")
        fo.write("G1 E-"+str(tray_value)+" ; this moves the extruder backwards, retracting the PCR tray\n\n")
        fo.write("G1 F2200\n\n")
        fo.write("G1 X250 F2200 ; this moves the x carriage to the next bath. the number after the F controls the speed (feedrate).\n\n")
        fo.write("G1 F"+str(feedrate)+"\n\n")
        fo.write("G1 E"+str(tray_value)+" F"+str(feedrate)+" ; Lower PCR tray (2500 steps is default value)\n\n")
        fo.write("G4 P30000 ; pause for 30 seconds\n\n")
        fo.write("G1 E-"+str(tray_value)+" F"+str(feedrate)+" ; Raise PCR tray (2500 steps is default value)\n\n")
        fo.write("G1 F2200\n\n")
        fo.write("G1 X-250 F2200 ; move PCR tray to first bath.\n\n")

        # Close Opened File
        fo.close()

elif comments in ('no','NO','No','n','N'):
        # Print Statement for Comments Diabled