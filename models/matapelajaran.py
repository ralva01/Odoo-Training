from odoo import models, fields, api

class CdnMataPelajaran(models.Model):
    _name = 'cdn.mata_pelajaran'
    _description = 'Cdn Mata Pelajaran'

    name = fields.Char(string='Nama Mata Pelajaran', required=True)
    kode_pelajaran = fields.Char(string='Kode Pelajaran', required=True, help='Kode unik untuk mata pelajaran')
    guru_id = fields.Many2one(comodel_name='cdn.guru', string='Guru Pengajar', required=True)
    kelas_ids = fields.Many2many(comodel_name='cdn.kelas', string='Kelas', help='Kelas yang diajarkan mata pelajaran')