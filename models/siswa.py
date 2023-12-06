from odoo import models, fields, api



class CdnSiswa(models.Model):
    _name = 'cdn.siswa'
    _description = 'Table Siswa'

    name = fields.Char(string= 'Nama Siswa', required=True)
    nis = fields.Char(string='NIS', required=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-Laki'), ('P', 'Perempuan'),],required=True)
    agama = fields.Selection(string='Agama', selection=[('Islam', 'Islam'), ('Kristen', 'Kristen'),('Buddha', 'Buddha'),])
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    no_tlp = fields.Char(string='No Handphone')
    alamat = fields.Text(string='')
    
    
    
    
    
    
    
    
