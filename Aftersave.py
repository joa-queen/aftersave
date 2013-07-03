import sublime, sublime_plugin, subprocess

class UglifyCommand(sublime_plugin.TextCommand):
	def run(self, text):
		trigger = "aftersave:"
		fl = self.view.substr(self.view.find("^(.+)\n", 0)).replace('/*', '').replace('*/', '').replace('//', '').replace('#', '').strip()
		if (fl[0:len(trigger)] == trigger):
			filename = self.view.file_name()
			cwd = self.view.file_name().split('/')[:-1]
			cwd = '/'.join(cwd)
			command = fl.replace(trigger, '').replace('<self>', filename).strip()
			p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
			out, stderr = p.communicate()

			print '[Aftersave] Executing: ' + command
			if (stderr):
				print '[Aftersave] error: ' + stderr
			if (out):
				print '[Aftersave] output: ' + out

class UglifySave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    view.run_command("uglify")