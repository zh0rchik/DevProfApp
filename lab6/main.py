from peewee import *
import cherrypy

# Подключение к базе данных
db = SqliteDatabase('database.db')
CP_CFG = {
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'C:/Users/georg/PycharmProjects/RPP/lab6'
    }
}


# Модель для таблицы История посещений
class VisitHistory(Model):
    id = AutoField()
    patient_name = CharField()
    doctor_name = CharField()
    reason = TextField()
    duration = IntegerField()

    class Meta:
        database = db


# Создание таблиц в базе данных
db.create_tables([VisitHistory])

# Класс-контроллер CherryPy
class WebInterface(object):
    @cherrypy.expose
    def index(self):
        # Получение всех объектов из базы данных
        visits = VisitHistory.select()

        # Генерация HTML-страницы для отображения посещений
        html = '<head><link rel="stylesheet" href="style.css"></head>'
        html += '<body><h1>История посещений поликлиники</h1>'
        html += '<table>'
        html += '<tr><th>№</th><th>ФИО пациента</th><th>ФИО врача</th><th>Причина обращения</th><th>Длительность</th></tr>'

        for visit in visits:
            html += f'<tr><td>{visit.id}</td><td>{visit.patient_name}</td><td>{visit.doctor_name}</td><td>{visit.reason}</td><td>{visit.duration}</td></tr>'

        html += '</table>'

        # Форма для добавления записей
        html += '''
            <h2>Добавить посещение:</h2>
            <form method="post" action="add_visit">
                <input type="text" name="patient_name" placeholder="ФИО пациента" required><br>
                <input type="text" name="doctor_name" placeholder="ФИО врача" required><br>
                <textarea name="reason" placeholder="Причина обращения" required></textarea><br>
                <input type="number" name="duration" placeholder="Длительность" required><br>
                <input type="submit" value="Добавить">
            </form>
        '''

        html += '</body>'

        return html

    @cherrypy.expose
    def add_visit(self, patient_name, doctor_name, reason, duration):
        # Создание нового объекта посещения
        visit = VisitHistory(patient_name=patient_name, doctor_name=doctor_name, reason=reason, duration=duration)
        visit.save()

        return 'Посещение успешно добавлено!'


# Конфигурация CherryPy
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080})

# Запуск CherryPy
cherrypy.quickstart(WebInterface(), config=CP_CFG)