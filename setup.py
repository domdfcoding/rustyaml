# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools_rust import RustExtension, Binding


setup(
	package_data={'': ['*']},
	rust_extensions=[RustExtension("rustyaml._rustyaml", "Cargo.toml", debug=False, binding=Binding.PyO3)],
	)
