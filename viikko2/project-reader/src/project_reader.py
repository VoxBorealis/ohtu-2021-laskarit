#import toml
import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        print("-------------------")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_content = tomli.loads(content)
        print(parsed_content)
        print("------------")
        print(parsed_content.keys())
        print("------alku------")
        print(parsed_content["tool"]["poetry"]["name"])
        print("------loppu------")


        return Project(parsed_content["tool"]["poetry"]["name"], parsed_content["tool"]["poetry"]["description"],
         parsed_content["tool"]["poetry"]["dependencies"], parsed_content["tool"]["poetry"]["dev-dependencies"])
