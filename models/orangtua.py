from odoo import models, fields, api



class CdnOrangtua(models.Model):
    _name = 'cdn.orangtua'
    _description = 'CdnOrangtua'

    name = fields.Char(string='Nama Orang Tua')
    nik = fields.Char(string='NIK', required=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-Laki'), ('P', 'Perempuan'),],required=True)
    agama = fields.Selection(string='Agama', selection=[('Islam', 'Islam'), ('Kristen', 'Kristen'),('Buddha', 'Buddha'),])
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    no_tlp = fields.Char(string='No Handphone')
    alamat = fields.Text(string='Alamat Lengkap')
    
    # Field One2many untuk menentukan siswa yang terkait dengan ayah dan ibu
    siswa_ayah_ids = fields.One2many(comodel_name='cdn.siswa', inverse_name='ayah_id')
    siswa_ibu_ids = fields.One2many(comodel_name='cdn.siswa', inverse_name='ibu_id')


    provinsi_id = fields.Many2one(comodel_name='cdn.provinsi', string='Provinsi')
    kota_id = fields.Many2one(comodel_name='cdn.kota', string='Kota')
    