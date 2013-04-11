import sublime, sublime_plugin
from datetime import datetime

class AddDateTimeStampCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit,self.view.sel()[0].begin(),datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
		self.view.run_command("insert_snippet",{"contents":"%s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

class AddDateStampCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		# self.view.insert(edit,self.view.sel()[0].begin(),datetime.now().strftime("%Y/%m/%d %H:%M"))
		self.view.run_command("insert_snippet",{"contents":"%s" % datetime.now().strftime("%Y-%m-%d %H:%M")})

class AddTimeStampCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		# self.view.insert(edit,self.view.sel()[0].begin(),datetime.now().strftime("%H:%M:%S"))
		self.view.run_command("insert_snippet",{"contents":"%s" % datetime.now().strftime("%H:%M:%S")})		

class TranslateStateOpenCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit,region,"OPEN")
				# selection = self.view.substr(region)
				# for line in selection.split('\n'):
				# 	if(line.find('Fixed')!=-1):
				# 		line.replace('Fixed','Open')
				# 	elif(line.find('Delay')!=-1):
				# 	    print "sss1"

class TranslateStateTodoCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit,region,"TODO")

class TranslateStateNextCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit,region,"NEXT")

class TranslateStateWorkCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit,region,"WORK")

class TranslateStateDoneCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for region in self.view.sel():
			if not region.empty():
				self.view.replace(edit,region,"DONE")