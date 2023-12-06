from odoo import models, fields, api



class CdnProvinsi(models.Model):
    _name = 'cdn.provinsi'
    _description = 'Cdn Provinsi'

    name = fields.Char(string='Provinsi')
    singkatan = fields.Char(string='Singkatan')




class CdnKota(models.Model):
    _name = 'cdn.kota'
    _description = 'Cdn Kota'

    name = fields.Char(string='Kota')
    singkatan = fields.Char(string='Singkatan')
    provinsi_id = fields.Many2one(comodel_name='cdn.provinsi', string='Provinsi')
    


    
