#!/usr/bin/awk -f
# input rsvp_sorted.csv | output guest_seat.csv

BEGIN {
    FS = ","
    table_number = 1
    seat_number = 1
    print "name,seat,table_number"
}

{
    guest_name = $1
    phone = $2
    number_guest = $4

    # Assign the guest to a table
    if (table_count[table_number] + number_guest <= 10) {
        table_count[table_number] += number_guest
        tally = 0
        for (i = 1; i <= number_guest; i++) {
            tally += 1
	    if ( i == 1) {
               print toupper(guest_name) " (" phone ")," seat_number "," table_number "#: " table_count[table_number]
            }
            else 
            if ( i == 2) {
               		print "PSGN " "#" i " " toupper(guest_name) "," seat_number "," table_number
            	}
            	else 
            	if ( i > 2) {
               		print "AHLI KLRG " "#" i " " toupper(guest_name) "," seat_number "," table_number "#: " table_count[table_number]
               		}
	   seat_number++
	   
        }
    } else {
        table_number++
        table_count[table_number] = number_guest
        for (i = 1; i <= number_guest; i++) {
            	    if ( i == 1) {
               print toupper(guest_name) " (" phone ")," seat_number "," table_number
            }
            else 
            if ( i == 2) {
               		print "PSGN " "#" i " " toupper(guest_name) "," seat_number "," table_number
            	}
            	else 
            	if ( i > 2) {
               		print "AHLI KLRG " "#" i " " toupper(guest_name) "," seat_number "," table_number
               		}
            seat_number++
        }
    }
}

END {
    print "Total tables: " table_number
}
