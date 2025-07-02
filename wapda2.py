
print(" === WAPDA BILLING === ")
custumer = input("enter custumer name: ")
units =float(input("units consumed: "))

if units <= 100:
   rate_per_unit =  5.0
elif units <= 200:
    rate_per_unit =  8.0
elif units <= 300:
    rate_per_unit =  10.0
else:
    rate_per_unit = 15.0

energy_charges = units * rate_per_unit

meter_charges = 150.0

sub_bill = energy_charges + meter_charges

gst = sub_bill * 0.17
 
total_bill = sub_bill + gst

print("\n--- WAPDA ELECTRICITY BILL ---")
print("custumer name   : " , custumer)
print("units consumed  : ", units)
print("rate per unit   : Rs. ",rate_per_unit)
print("energy charges  : Rs.",energy_charges )
print("meter charge    : Rs.", meter_charges)
print("subtotal        : Rs.", sub_bill)
print("GST 17%         : Rs.",round(gst, 2))
print("total bill      : Rs.",round(total_bill, 2))
