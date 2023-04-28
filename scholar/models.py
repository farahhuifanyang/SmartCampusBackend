from django.db import models


class ScholarBasicInfo(models.Model):
    sid = models.IntegerField(primary_key=True)
    chinese_name = models.TextField()
    gender = models.TextField()
    department = models.TextField()
    center = models.TextField()
    title = models.TextField()
    degree = models.TextField()
    job = models.TextField()
    field = models.TextField()
    organization = models.TextField()
    introduction = models.TextField()
    thanks_paper = models.TextField()
    mag_paper = models.TextField()
    co_scholar = models.TextField()
    keywords = models.TextField()

    def get_dict(self):
        attr_name_lt = [a.name for a in self._meta.get_fields()]
        d = {name: self.__getattribute__(name) for name in attr_name_lt}
        return d


class TeacherStudents(models.Model):
    tid = models.IntegerField(primary_key=True)
    name = models.TextField()
    students = models.TextField()

    def get_dict(self):
        attr_name_lt = [a.name for a in self._meta.get_fields()]
        d = {name: self.__getattribute__(name) for name in attr_name_lt}
        return d


class Papers(models.Model):
    url = models.TextField(null=True)
    volume = models.TextField(null=True)
    fos = models.TextField(null=True)
    issue = models.TextField(null=True)
    year = models.IntegerField(null=True)
    authors = models.TextField(null=True)
    lang = models.TextField(null=True)
    doc_type = models.TextField(null=True)
    page_end = models.TextField(null=True)
    publisher = models.TextField(null=True)
    n_citation = models.IntegerField(null=True)
    abstract = models.TextField(null=True)
    venue = models.TextField(null=True)
    page_start = models.TextField(null=True)
    doi = models.TextField(null=True)
    title = models.TextField(null=True)
    id = models.TextField(primary_key=True)
    keyword = models.TextField(null=True)

    def get_dict(self):
        attr_name_lt = [a.name for a in self._meta.get_fields()]
        d = {name: self.__getattribute__(name) for name in attr_name_lt}
        return d


class ByAuthorPaper(models.Model):
    by_author = models.TextField()
    paper_id = models.TextField()


class PaperReferences(models.Model):
    citing = models.TextField()
    cited = models.TextField()
