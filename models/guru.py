from odoo import models, fields, api



class CdnGuru(models.Model):
    _name = 'cdn.guru'
    _description = 'Cdn Guru'

    name = fields.Char(string= 'Nama Guru', required=True)
    nip = fields.Char(string='NIP', required=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-Laki'), ('P', 'Perempuan'),],required=True)
    agama = fields.Selection(string='Agama', selection=[('Islam', 'Islam'), ('Kristen', 'Kristen'),('Buddha', 'Buddha'),])
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    no_tlp = fields.Char(string='No Handphone')
    alamat = fields.Text(string='Alamat Lengkap')
    provinsi_id = fields.Many2one(comodel_name='cdn.provinsi', string='Provinsi')
    kota_id = fields.Many2one(comodel_name='cdn.kota', string='Kota')
    
     # Relasi ke kelas (One2many)
    kelas_id = fields.One2many(comodel_name='cdn.kelas', inverse_name='wali_kelas_id', string='Kelas')
    # Field Boolean untuk menandai apakah guru sudah menjadi wali kelas atau belum
    is_wali_kelas = fields.Boolean(string='Wali Kelas', compute='_compute_is_wali_kelas', store=True)
    mata_pelajaran_ids = fields.One2many(comodel_name='cdn.mata_pelajaran', inverse_name='guru_id', string='Mata Pelajaran')

    @api.depends('kelas_id')
    def _compute_is_wali_kelas(self):
        for guru in self:
            guru.is_wali_kelas = bool(guru.kelas_id)
    
