#!/usr/bin/awk -f
# input rsvp_sorted.csv | output guest_seat.csv

BEGIN {
    FS = ","
    table_number = 1
    seat_number = 1
    print "name,seat,table_number"
}

function toTitle(str) {
    #gsub(/(^|[^a-zA-Z])([a-z])/g, function (match, p1, p2) { return toupper(p2); }, str)
    #return str
}

{
    guest_name = $1
    phone = "0"$2
    number_guest = $4

    # Assign the guest to a table
    if (table_count[table_number] + number_guest <= 10) {
        table_count[table_number] += number_guest
        for (i = 1; i <= number_guest; i++) {
            if (i == 1) {
                print toupper(guest_name) " (" phone ")," seat_number "," table_number
            } else {
                print "AHLI KELUARGA " "#" i " " toupper(guest_name) "," seat_number "," table_number
            }
            seat_number++
        }
    } else if (table_count[table_number] < 10) {
        # Assign as reserve with count
        m = 10 - table_count[table_number]
        for (n = 1; n <= m; n++) {
            print "SIMPANAN " "#" table_number ":" seat_number "," seat_number "," table_number
            seat_number++
        }
        table_number++
    } else {
        table_number++
        table_count[table_number] = number_guest
        for (i = 1; i <= number_guest; i++) {
           if (i == 1) {
                print toupper(guest_name) " (" phone ")," seat_number "," table_number
            } else {
                print "AHLI KELUARGA " "#" i " " toupper(guest_name) "," seat_number "," table_number
            }
            seat_number++
        }
    }
}

END {
    print "Total tables: " table_number
}
