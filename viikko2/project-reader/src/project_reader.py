from urllib import request
from project import Project
from tomlkit import parse


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # Deserialisointi/parsinta
        content_dict = parse(content)

        deps, dev_deps = [], []
        for dep in content_dict["tool"]["poetry"]["dependencies"]:
            deps.append(dep)
        for dep in content_dict["tool"]["poetry"]["dev-dependencies"]:
            dev_deps.append(dep)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            content_dict["tool"]["poetry"]["name"], 
            content_dict["tool"]["poetry"]["description"], 
            deps, dev_deps
        )
