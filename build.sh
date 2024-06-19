echo " BUIL START"
python3.10.13 -m pip install -r requirements.txt
python3.10.13 manage.py collectstatic --noinput --clear
echo " BUIL END"