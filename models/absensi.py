from odoo import models, fields, api

class CdnAbsensi(models.Model):
    _name = 'cdn.absensi'
    _description = 'Cdn Absensi'

    name = fields.Char(string='Nama Absensi', required=True)
    tanggal_absen = fields.Date(string='Tanggal Absen', required=True, default=fields.Date.today())
    kelas_id = fields.Many2one(comodel_name='cdn.kelas', string='Kelas', required=True)
    siswa_ids = fields.Many2many(comodel_name='cdn.siswa', string='Siswa', required=True)
    keterangan = fields.Text(string='Keterangan')

    @api.onchange('kelas_id')
    def _onchange_kelas_id(self):
        # Filter siswa berdasarkan kelas yang dipilih
        return {'domain': {'siswa_ids': [('kelas_id', '=', self.kelas_id.id)]}}
