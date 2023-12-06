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
    alamat = fields.Text(string='Alamat Lengkap')
    provinsi_id = fields.Many2one(comodel_name='cdn.provinsi', string='Provinsi')
    kota_id = fields.Many2one(comodel_name='cdn.kota', string='Kota')

    orangtua_id = fields.Many2one(comodel_name='cdn.orangtua', string='Nama Orang Tua')
    
    ayah_id = fields.Many2one(comodel_name='cdn.orangtua', string='Ayah')
    ibu_id = fields.Many2one(comodel_name='cdn.orangtua', string='Ibu')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
