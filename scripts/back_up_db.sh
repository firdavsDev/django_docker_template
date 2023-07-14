#!Back up database:
#docker exec -t <database-container> pg_dump -c -U <database-user> -d <database-name> > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
docker exec -t a50125188788 pg_dump -c -U {name}_user -d {name}_db > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
