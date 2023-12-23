import setuptools
import shamir

#sudo apt install libldap2-dev
setuptools.setup(
    name="shamir",
    version=shamir.version,
    python_requires=">=3.8",
    author="Bryan Gillespie",
    author_email="Bryan.Gillespie@colostate.edu",
    description="Shamir secret sharing for BIP-0039 seed phrases",
    url="https://github.com/bgillesp/shamir",
    packages=["shamir"],
    install_requires=['mnemonic', 'typing', 'click', 'pathlib'],
    include_package_data=True,
    package_data={"shamir": ["data/*.dat", 'adapters/**']},
    entry_points={
        'console_scripts': [
            'shamir = shamir.cli:cli',
        ],
    },
)
