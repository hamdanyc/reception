# Load necessary library
library(dplyr)

# Read the CSV file
guests <- read.csv('guest_lst.csv')

# Function to assign seats based on family_id and handle single guests
assign_seats <- function(guests) {
  # Sort guests by family_id (if not NULL) and name to ensure families are seated together
  sorted_guests <- guests %>%
    arrange(ifelse(is.na(family_id), Inf, family_id), name)
  
  # Initialize seat assignment
  seat_assignment <- data.frame(
    name = sorted_guests$name,
    family_id = sorted_guests$family_id,
    table_number = NA,
    seat_number = NA
  )
  
  # Assign seats
  table_count <- 1
  seat_count <- 1
  
  for (i in 1:nrow(sorted_guests)) {
    if (seat_count > 10) {
      table_count <- table_count + 1
      seat_count <- 1
    }
    
    seat_assignment$table_number[i] <- table_count
    seat_assignment$seat_number[i] <- seat_count
    
    seat_count <- seat_count + 1
  }
  
  return(seat_assignment)
}

# Assign seats to guests
seating_arrangement <- assign_seats(guests)

# Write the seating arrangement to a CSV file
write.csv(seating_arrangement, 'guest_seat.csv', row.names = FALSE)
