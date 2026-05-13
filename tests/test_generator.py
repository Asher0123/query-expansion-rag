from src.mock_generator import GenerativeModel


def test_aws_expansion():

    generator = GenerativeModel()

    query = "What is aws?"

    expanded = generator.generate_content(query)

    assert "Amazon Web Services" in expanded.text


def test_vpc_expansion():

    generator = GenerativeModel()

    query = "aws vpc"

    expanded = generator.generate_content(query)

    assert "Virtual Private Cloud" in expanded.text


def test_peak_load_paraphrase():

    generator = GenerativeModel()

    query = "How does AWS handle peak load?"

    expanded = generator.generate_content(query)

    valid_expansions = [
        "high traffic",
        "heavy workloads",
        "traffic spikes"
    ]

    assert any(
        phrase in expanded.text
        for phrase in valid_expansions
    )