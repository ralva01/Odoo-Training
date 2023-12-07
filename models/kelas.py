from odoo import models, fields, api



class CdnKelas(models.Model):
    _name = 'cdn.kelas'
    _description = 'Cdn Kelas'
    _rec_name = 'nama_kel'

    nama_kel = fields.Selection (string='Kelas', 
        selection=
        [('7A', '7A'), ('7B', '7B'), ('7C', '7C'),
        ('8A', '8A'), ('8B', '8B'), ('8C', '8C'),
        ('9A', '9A'), ('9B', '9B'), ('9C', '9C'),
        ])
    
    guru_id = fields.Many2one(comodel_name='cdn.guru', string='Wali Kelas')
    details_id = fields.Many2many(comodel_name='cdn.siswa', string='Nama Siswa')
    






    
    
