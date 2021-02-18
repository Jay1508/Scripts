The intent of this script is to see references to external devices using vendor identifier (VID) and product identifier (PID).
 these values are represented by four hexadecimal characters. In cases where the vendor and product name are not identified, the examiner must look up this information.
 One such location for this information is the following web page: http://linux-usb.org/usb.ids. For example, on this web page, we can see that a Kingston DataTraveler G3 has a VID of 0951 and a PID of 1643.
 We will use this data source when attempting to identify vendor and product names by using the defined identifiers.

 he usb_lookup.py script requires two arguments—vendor and product IDs for the USB of interest. We can find this information by looking at a suspect HKLM\SYSTEM\%CurrentControlSet%\Enum\USB registry key.
 For example, supplying the vendor, 0951, and product, 1643, from the sub-key VID_0951&PID_1643, results in our script identifying the device as a Kingston DataTraveler G3:

 C:\Users\Jamal\Documents\Certifications & Vendors\GitHub\Scripts\USB lookup>python usb_lookup.py 0951 1643
Vendor: Kingston Technology
Product: DataTraveler G3
