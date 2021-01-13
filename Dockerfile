FROM python:3.9
# Create app directory
WORKDIR /home/cypher

# Install app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Bundle app source
COPY . /home/cypher

RUN ls

EXPOSE 8000

CMD [ "python", "manage.py runserver" ]