echo "seat allocation -- start"
/home/abi/reserve/.venv/bin/python /home/abi/reserve/seat_alloc.py
sed -i 's/Lh/LVH/g;s/Tudm/TUDM/g;s/Tldm/TLDM/g;s/Apmm/APMM/g;s/Jhev/JHEV/g;s/Pvatm/PVATM/g;s/Ramd/RAMD/g;s/Pgb/PGB/g;s/Kagat/KAGAT/g;s/Ugat/UGAT/g;s/Ydp/YDP/g;s/Ppp/PPP/g;s/Ydp/YDP/g;s/Adc/ADC/g;s/Hs/HS/g' guest_seat.csv
/home/abi/reserve/.venv/bin/python /home/abi/reserve/guest_seat_pdf.py
/home/abi/reserve/.venv/bin/python /home/abi/reserve/guest_seat_analyzer.py
/home/abi/reserve/.venv/bin/python /home/abi/reserve/guest_list.py
echo "seat allocation -- done"
