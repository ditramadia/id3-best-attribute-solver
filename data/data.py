'''

Formatting
data = {
  [ <attribute-1>, <row-1-of-attribute-1>, <row-2-of-attribute-1>, ... ]
  [ <attribute-2>, <row-1-of-attribute-2>, <row-2-of-attribute-2>, ... ]
  [ <attribute-3>, <row-1-of-attribute-3>, <row-2-of-attribute-3>, ... ]
  [ <target-attribute>, <row-1-of-target-attribute>, <row-2-of-target-attribute>, ... ]
}


'''
# Format
# data = {
# }

# Contoh Soal
#
# data = [
#   ["Outlook", "Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny", "Sunny", "Rain", "Sunny", "Overcast", "Overcast", "Rain",],
#   ["Temperature", "Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
#   ["Humidity", "High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
#   ["Wind", "Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Strong"], 
#   ["Play Tennis", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"], 
# ]
#
# Jawaban
# 
# Outlook -> Humidity -> Wind -> Temperature

# Latihan Soal
#
data = [
  ["Deadline", "Urgent", "Urgent", "Dekat", "Tidak ada", "Tidak ada", "Tidak ada", "Dekat", "Dekat", "Dekat", "Urgent"],
  ["Hangout", "Ya", "Tidak", "Ya", "Ya", "Tidak", "Ya", "Tidak", "Tidak", "Ya", "Tidak"],
  ["Malas", "Ya", "Ya", "Ya", "Tidak", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Tidak"],
  ["Aktivitas", "Kumpul-kumpul", "Belajar", "Kumpul-kumpul", "Kumpul-kumpul", "Jalan-jalan ke mall", "Kumpul-kumpul", "Belajar", "Nonton TV", "Kumpul-kumpul", "Belajar"]
]

# Jawaban
# 
# Hangout -> Deadline -> Malas