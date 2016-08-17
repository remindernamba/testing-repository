#coding: utf-8
from lettuce import before, after, world
from selenium import webdriver
from mapping import site_mapping

@before.harvest
def setup(server):
    # world - переменная, используемая lettuce между всеми стадиями тестов, т.е. хранящая в себе информацию между тестами
    world.browser = webdriver.Firefox() # открываем браузер
    world.mapping = site_mapping # сохраняем структуру в world


@after.all
def teardown(total):
    world.browser.close()
