from IPython.display import Markdown as md

def show_table(header,datas,format=None):
  cols = len(header)
  header = "|" + "|".join(header) + "|"
  if format == None:
    format = []
    for col in range(cols):
      format.append("---")
  format = "|" + "|".join(format) + "|"
  table = header
  table += "\n"
  table += format
  table += "\n"
  for data in datas:
    table += "|" + "|".join(data) + "|"
    table += "\n"
  md(table)
