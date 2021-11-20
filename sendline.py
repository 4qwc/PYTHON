from songline import Sendline


pic1 = 'https://cdn.pixabay.com/photo/2020/06/13/03/40/flower-5292556_1280.jpg'
pic2 = 'https://media.istockphoto.com/photos/golden-buddha-statue-on-sunrise-background-picture-id1058800400?k=20&m=1058800400&s=612x612&w=0&h=nILHnGCJXwUCginaLNeFk84p33COIdTxR1uxv5iJJxk='

m = Sendline('VdgrMdDalgmdkEH3MRMpPVoDNrprmGM7K6FWvM3we5k') # token line notify

m.sendtext('ทดสอบส่งข้อความไลน์')

m.sticker(618,4)
m.sticker(622,4)

m.sendimage(pic2)