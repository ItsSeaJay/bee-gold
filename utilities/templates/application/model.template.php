<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class {name} extends CI_Model {{

    private $table = '{table}';

    public function __construct()
    {{
        parent::__construct();
        $this->load->database();
    }}
}}