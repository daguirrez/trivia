import abc
from trivia import Category, Match
from storage import MyStorage

class IScreen(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def draw(self):
		pass

class TitleScreen(IScreen):
	def draw(self):
		title = '''
		───────────────────────────────────────────────────────────────────────────────────────
		─██████████████─████████████████───██████████─██████──██████─██████████─██████████████─
		─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░██─██░░██──██░░██─██░░░░░░██─██░░░░░░░░░░██─
		─██████░░██████─██░░████████░░██───████░░████─██░░██──██░░██─████░░████─██░░██████░░██─
		─────██░░██─────██░░██────██░░██─────██░░██───██░░██──██░░██───██░░██───██░░██──██░░██─
		─────██░░██─────██░░████████░░██─────██░░██───██░░██──██░░██───██░░██───██░░██████░░██─
		─────██░░██─────██░░░░░░░░░░░░██─────██░░██───██░░██──██░░██───██░░██───██░░░░░░░░░░██─
		─────██░░██─────██░░██████░░████─────██░░██───██░░██──██░░██───██░░██───██░░██████░░██─
		─────██░░██─────██░░██──██░░██───────██░░██───██░░░░██░░░░██───██░░██───██░░██──██░░██─
		─────██░░██─────██░░██──██░░██████─████░░████─████░░░░░░████─████░░████─██░░██──██░░██─
		─────██░░██─────██░░██──██░░░░░░██─██░░░░░░██───████░░████───██░░░░░░██─██░░██──██░░██─
		─────██████─────██████──██████████─██████████─────██████─────██████████─██████──██████─
		───────────────────────────────────────────────────────────────────────────────────────
		────────────────────────────────────────────────────────────────────────
		─██████████████─██████████─██████──────────██████─██████████████─██████─
		─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─██░░██─
		─██████░░██████─████░░████─██░░░░░░░░░░░░░░░░░░██─██░░██████████─██░░██─
		─────██░░██───────██░░██───██░░██████░░██████░░██─██░░██─────────██░░██─
		─────██░░██───────██░░██───██░░██──██░░██──██░░██─██░░██████████─██░░██─
		─────██░░██───────██░░██───██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██─
		─────██░░██───────██░░██───██░░██──██████──██░░██─██░░██████████─██████─
		─────██░░██───────██░░██───██░░██──────────██░░██─██░░██────────────────
		─────██░░██─────████░░████─██░░██──────────██░░██─██░░██████████─██████─
		─────██░░██─────██░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██─
		─────██████─────██████████─██████──────────██████─██████████████─██████─
		────────────────────────────────────────────────────────────────────────
		
		Enter your player name in three letters:'''
		return title

class MenuScreen(IScreen):
	def draw(self):
		menu = '''
		In this game you will be able to experience a 
		trivia of some of the most interesting topics
		currently.

		Menu:
		Play match (writes 1)
		View player stats(writes 2)'''
		return menu

class PlayerStatsScreen(IScreen):
	def __init__(self, player, mystorage):
		self.__player = player
		self.__mystorage = mystorage
	
	def draw(self):
		stats = f'''
		Yout stats are:

		{self.__mystorage.load_player_statistics(self.__player)}''' 
		return stats

class CategoriesScreen(IScreen):
	def __init__(self, category):
		self.__category = category

	def draw(self):
		categoriesstr = '''
		Select the category of your trivia. if you 
		don't select any of the default category is 
		Anime & Manga. (Introduce the id)

		Categories:

		{for q in self.__category:
			q.name + " writes " + q.__id}'''
		return categoriesstr


class GameScreen(IScreen):
	def __init__(self, match):
		self.__match = match

	def draw(self):
		qa = f'''
		Read the question and select the answer you 
		think is right.

		Question: {self.__match.questions[self.__match.index].get_question()}
					
		Possible answers:
		{self.__match.questions[self.__match.index].get_answers()}'''
		return qa

class FinalScreen(IScreen):
	def __init__(self, match):
		self.__match = match

	def draw(self):
		result = len([q for q in self.__match.questions if q.is_correct])
		
		final1 = '''
		Results:

		╔═╗───╔═╗───╔╗
		║╬╠═╦╦╣═╬═╦═╣╚╗
		║╔╣╩╣╔╣╔╣╩╣═╣╔╣
		╚╝╚═╩╝╚╝╚═╩═╩═╝

		You answered all the questions correctly.'''

		final2 = '''
		Results:

		╔═╦╦╗────╔╗
		║║║╠╬═╦═╗║╚╦╦╦╦╗
		║║║║║═╣╩╣║╔╣╔╣║║
		╚╩═╩╩═╩═╝╚═╩╝╠╗║
		─────────────╚═╝

		You answered 7 to 9 correct questions.'''

		final3 = '''
		Results:

		╔═╦╗──────────────╔╗──╔╗──╔╗╔╗
		╚╗║╠═╦╦╗╔═╦═╗╔═╦╗╔╝╠═╗║╚╦═╣╚╣╚╦═╦╦╗
		╔╩╗║╬║║║║═╣╬╚╣║║║║╬║╬║║╬║╩╣╔╣╔╣╩╣╔╝
		╚══╩═╩═╝╚═╩══╩╩═╝╚═╩═╝╚═╩═╩═╩═╩═╩╝

		You answered 4 to 6 correct questions.'''

		final4 = '''
		Results:

		╔═╦╗────╔═╦╗───────╔╗──────────────────╔╗╔╗
		╚╗║╠═╦╦╗║═╣╚╦═╦╦╦╗╔╝║╔═╦╗╔═╗╔╦╗╔═╗╔═╦╦═╣╚╣╚╦═╦╦╗╔═╦═╗╔══╦═╗
		╔╩╗║╬║║║╠═║║║╬║║║╚╣╬║║╬║╚╣╬╚╣║║║╬╚╣║║║╬║╔╣║║╩╣╔╝║╬║╬╚╣║║║╩╣
		╚══╩═╩═╝╚═╩╩╩═╩═╩═╩═╝║╔╩═╩══╬╗║╚══╩╩═╩═╩═╩╩╩═╩╝─╠╗╠══╩╩╩╩═╝
		─────────────────────╚╝─────╚═╝─────────────────╚═╝

		You answered 1 to 3 correct questions.'''

		if result == 10:
			return final1
		
		if result >= 7 and result <= 9:
			return final2
		
		if result >= 4 and result <= 6:
			return final3
		
		return final4