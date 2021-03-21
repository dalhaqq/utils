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
    data = [str(x) for x in data]
    table += "|" + "|".join(data) + "|"
    table += "\n"
  return table
