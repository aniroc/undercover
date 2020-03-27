#Undercover

Shopping Cart setup instructions:

Django
Postgres:  Postgres.app V12 (on Mac)

1.  Setup
	Install Postgres if not already installed

2.  Install and start virtual environent:
	source undercover/bin/activate

4.  Download or check out from github and change to directory
	https://github.com/aniroc/undercover.git

3.  Install requirements:
	cat requirements.txt | xargs -n 1 pip install

5.  Create required database tables. (Note: tables kept in public schema)
	cd undercover
	python manage.py migrate

6.  Start Django:

7.  Populate Product table:
	accesses external API and either:
		1. Creates new entry if item does not exist in the db table

		2. 	Updates table price for item (i.e. Monthy update) by opening a command window & issuing:

		curl --location --request GET 'http://127.0.0.1:8000/excursions/update_tickets/?name=update'

	Default qoh is set to 10. (for now)

7.  Install Memecache (already configured in core/settings.py):
		Installed via:
		brew install memcached

		See requirements for additional related packages.

		To run memecache
		memcached -l 127.0.0.1:11211

		To see memecache status (make sure it is running):
		user: tourist. pwd: tourist01
		http://127.0.0.1:8000/admin/

8.  Access Shopping Cart & purchase Tickets

	http://127.0.0.1:8000/


Extra API info:
Update API:
accesses external API and either:
1. Creates new entry if item does not exist in the db table
2. Updates table price for item (i.e. Monthy update).
http://127.0.0.1:8000/excursions/update_tickets/?name=update


Additional APIs (for further integration into another front end):
http://127.0.0.1:8000/excursions/tickets/
http://127.0.0.1:8000/excursions/ticket_detail-api/103/


