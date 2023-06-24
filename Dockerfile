FROM python:3.7-alpine as builder

WORKDIR '/usr/app'

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","-m","pytest","--html=reports/reports.html"]

# copy command
#If src is a directory, the entire contents of the directory are copied, including filesystem metadata.

#Note: The directory itself is not copied, just its contents.

FROM nginx
COPY --from=builder /usr/app/reports /usr/share/nginx/html

# since copy cmd will copy entire content of reoprts folder inside which a reports.html file is
# so use http://www.localhost:port/reports.html as link to view reoprts file.

