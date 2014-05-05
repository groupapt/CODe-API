<?php

class Json extends CI_Controller {
	function index() {
		$this->load->view( 'api-json-content-type' );
		echo '{"error": "No method specified!"}';
	}
}