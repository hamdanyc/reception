#!/usr/bin/awk -f

BEGIN {
    FS = ","
    table_number = 1
    seat_number = 1
    print "name,seat,table_number"
}

{
    guest_name = $1
    phone = $2
    number_guest = $3

    # Assign the guest to a table
    if (table_count[table_number] + number_guest <= 10) {
        table_count[table_number] += number_guest
        for (i = 1; i <= number_guest; i++) {
	    if ( i == 1) {
               print toupper(guest_name) " (" phone ")," seat_number "," table_number
            }
            else {
               print "PASANGAN|AHLI KELUARGA " "#" i " " toupper(guest_name) "," seat_number "," table_number
            }
	   seat_number++
        }
    } else {
        table_number++
        table_count[table_number] = number_guest
        for (i = 1; i <= number_guest; i++) {
            print "PASANGAN|AHLI KELUARGA " "#" i " " toupper(guest_name) "," seat_number "," table_number
            seat_number++
        }
    }
}

END {
    print "Total tables: " table_number
}
