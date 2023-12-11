from odoo import models, fields, api



class CdnKelas(models.Model):
    _name = 'cdn.kelas'
    _description = 'Cdn Kelas'
    _rec_name = 'nama_kel'

    nama_kel = fields.Selection(
        string='Kelas', 
        selection=[
            ('7A', '7A'), ('7B', '7B'), ('7C', '7C'),
            ('8A', '8A'), ('8B', '8B'), ('8C', '8C'),
            ('9A', '9A'), ('9B', '9B'), ('9C', '9C'),
        ]
    )
    
    details_id = fields.Many2many(comodel_name='cdn.siswa', string='Nama Siswa', domain="[('id', 'not in', details_id)]")
    wali_kelas_id = fields.Many2one(comodel_name='cdn.guru', string='Wali Kelas')
    absensi_ids = fields.One2many(comodel_name='cdn.absensi', inverse_name='kelas_id', string='Absensi')

    #jumlah_siswa = fields.Integer(string='Jumlah Siswa', compute='_compute_jumlah_siswa', store=True)
    jumlah_siswa_laki_laki = fields.Integer(string='Jumlah Siswa Laki-laki', compute='_compute_jumlah_siswa_per_jenis_kelamin', store=True)
    jumlah_siswa_perempuan = fields.Integer(string='Jumlah Siswa Perempuan', compute='_compute_jumlah_siswa_per_jenis_kelamin', store=True)
    
    #@api.depends('details_id')
    #def _compute_jumlah_siswa(self):
        #for kelas in self:
            #kelas.jumlah_siswa = len(kelas.details_id)

    @api.depends('details_id.jenis_kel')
    def _compute_jumlah_siswa_per_jenis_kelamin(self):
        for kelas in self:
            siswa_laki_laki = kelas.details_id.filtered(lambda x: x.jenis_kel == 'l')
            siswa_perempuan = kelas.details_id.filtered(lambda x: x.jenis_kel == 'P')
            kelas.jumlah_siswa_laki_laki = len(siswa_laki_laki)
            kelas.jumlah_siswa_perempuan = len(siswa_perempuan)

    @api.onchange('details_id')
    def _onchange_details_id(self):
         #Proses penyimpanan perubahan ke tabel siswa
        #Misalnya, menyimpan perubahan ke field di tabel siswa
        for siswa in self.details_id:
            siswa.write({'kelas_id': self.id})

    #@api.ondelete(at_uninstall=True)
    #def _ondelete_cdn_kelas(self):
        # Proses yang ingin Anda lakukan saat model cdn.kelas dihapus
        # Misalnya, menghapus referensi kelas_id pada semua siswa yang terkait
        #for siswa in self.details_id:
            #siswa.write({'kelas_id': False})
