#Name: Jake Lorah
#Date: 09/11/2018
#Program Number: Volume.py
#Program Description: This program computes the volume (in liters) of a six-pack of soda.



#Cans and the total volume of a six-pack and a two-liter bottle

#Liters in a 12-ounce can a two-liter bottle

CAN_VOLUME=0.355
BOTTLE_VOLUME=2.0

#Number of cans per pack
CansPerPack=6

#Calculate total volume in the cans
totalVolume=CansPerPack*CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "liters.")

#Calculate total volume in the cans and a two-liter bottle
totalVolume=totalVolume+BOTTLE_VOLUME
print("A six-pack and a two-liter bottle contains", totalVolume, "liters.")

