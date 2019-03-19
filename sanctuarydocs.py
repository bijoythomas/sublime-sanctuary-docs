import sublime, sublime_plugin
from urllib.request import urlopen
import re

class SanctuaryDocsCommand(sublime_plugin.WindowCommand):
  def run(self):
    window = self.window
    view = window.active_view()
    sel = view.sel()
    region1 = sel[0]
    selectionText = view.substr(region1)
    if selectionText:
      self.fetchDoc(selectionText)
    else:
      self.window.show_input_panel('Enter a sanctuary function', '', self.fetchDoc, None, None)

  def append_data(self, data):
    self.sanctuary_docs_view.set_read_only(False)
    self.sanctuary_docs_view.run_command('insert_snippet', {'contents': data})
    self.sanctuary_docs_view.set_read_only(True)

  def show_docs_panel(self, fn):
    # data = urlopen('https://raw.githubusercontent.com/ramda/ramda/v0.24.1/src/' + text + '.js')
    data = urlopen('https://raw.githubusercontent.com/sanctuary-js/sanctuary/master/index.js')
    text = data.read().decode('utf-8')
    search = re.compile(r"(\/\/# "+ re.escape(fn) + r" ::.*?)```$", re.MULTILINE|re.DOTALL)
    v = search.findall(text)
    lines = v[0].split('\n')
    doc = '\n'.join(map(lambda line: line.strip(), map(lambda line: line.replace('//.', ''), filter(lambda line: "```javascript" not in line, lines))))
    self.append_data(doc)
    self.window.run_command('show_panel', {'panel': 'output.sanctuary_docs_view'})

  def fetchDoc(self, text):
    if not hasattr(self, 'sanctuary_docs_view'):
      hasattr(self, 'sanctuary_docs_view')
    self.sanctuary_docs_view = self.window.get_output_panel('sanctuary_docs_view')
    try:
      self.show_docs_panel(text)
    except Exception as e:
      print(e)
      self.append_data('No such function')
      self.window.run_command('show_panel', {'panel': 'output.sanctuary_docs_view'})