
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))
import orfs
import pytest


def test_orfs_basic_output(capsys):
	# Simple DNA sequence with a known ORF in frame 1
	dna = "ATGGGGTAA"  # ATG (start, M), GGG (G), TAA (stop)
	orfs.orfs(dna)
	captured = capsys.readouterr()
	assert "Forward Strand Frame 1:" in captured.out
	assert "MG" in captured.out  # Depending on translation function

def test_orfs_reverse_output(capsys):
	# DNA with a reverse complement ORF
	dna = "TTTACCCAT"  # Reverse complement is ATGGGTAAA
	orfs.orfs(dna)
	captured = capsys.readouterr()
	assert "Reverse Strand Frame 1:" in captured.out

def test_orfs_no_orf(capsys):
	# DNA with no start codon
	dna = "CCCCCCCCC"
	orfs.orfs(dna)
	captured = capsys.readouterr()
	assert "M" not in captured.out  # No methionine should be found

def test_orfs_logging(monkeypatch):
	# Test that logger.info is called
	called = {}
	def fake_info(msg):
		called['info'] = msg
	monkeypatch.setattr(orfs.logger, 'info', fake_info)
	orfs.orfs("ATGGGGTAA")
	assert 'Running orfs for' in called['info']