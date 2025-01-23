# Variables
k_electric: str = "on"  # بجلی کی موجودہ حالت
ups: str = "off"        # یو پی ایس کی موجودہ حالت

# حالات کے مطابق پرنٹ کرنا
print(k_electric == "on" and ups == "off")  # بجلی آئے تو یو پی ایس بند ہو - True
print(k_electric == "off" and ups == "on")  # بجلی جائے تو یو پی ایس چالو ہو - True
print(k_electric == "off" and ups == "off")  # دونوں بند ہوں - False
print(k_electric == "on" and ups == "on")  # دونوں آن ہوں - False

# دیگر ممکنہ حالتوں کی جانچ
k_electric = "off"
ups = "on"
print(k_electric == "on" and ups == "off")  # False
print(k_electric == "off" and ups == "on")  # True
print(k_electric == "off" and ups == "off")  # False
print(k_electric == "on" and ups == "on")  # False

# Strings and Variables
k_electric: str = "no electricity"
ups: str = "no ups"
generator: str = "working"

# Examples of True and False conditions
print("Example 1:")
print(k_electric == ups)  # False, as both strings are different

print("\nExample 2:")
print(ups != generator)  # True, as "no ups" is not equal to "working"

print("\nExample 3:")
result = k_electric == "no electricity" and generator == "working"
print("Is electricity off and generator working? ", result)  # True

print("\nExample 4:")
result = k_electric == "electricity available" or ups == "no ups"
print("Is electricity available or UPS not working? ", result)  # True

# Printing Results in Different Ways
print("\nDifferent Printing Styles:")
# 1. Using f-string
print(f"k_electric and ups are equal: {k_electric == ups}")

# 2. Using format()
print("UPS status is same as generator: {}".format(ups == generator))

# 3. Direct concatenation
print("Electricity status: " + ("No electricity" if k_electric == "no electricity" else "Available"))

# 4. Conditional inline check
print("Generator is working!" if generator == "working" else "Generator is off.")
