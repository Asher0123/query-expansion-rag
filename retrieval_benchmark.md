# Retrieval Benchmark Comparison

## Query 1

### Original Query
What is AWS?

### Enhanced Query
What is Amazon Web Service Cloud Computing?

---

## Strategy A — Raw Retrieval

| Rank | Page | Chunk Summary                                          | Relevance  |
|------|------|--------------------------------------------------------|------------|
| 1    | 10   | Introduction to AWS infrastructure and cloud computing | High       |
| 2    | 9    | AWS deployment and scalability benefits                | Medium     |
| 3    | 9    | AWS cloud services and infrastructure overview         | Medium     |
| 4    | 36   | AWS Solutions Architect and SysOps roles               | Low        |

---

## Strategy B — Enhanced Retrieval

| Rank | Page | Chunk Summary                                              | Relevance  |
|------|------|------------------------------------------------------------|------------|
| 1    | 8    | AWS cloud computing platform and security/storage services | High       |
| 2    | 10   | AWS infrastructure, elasticity, and scalability            | High       |
| 3    | 11   | Cloud computing concepts and AWS EC2                       | High       |
| 4    | 8    | AWS on-demand cloud computing model                        | Medium     |

---

## Precision@4 Evaluation

|           Strategy             | Relevant Chunks | Total Retrieved | Precision@4 |
|--------------------------------|-----------------|-----------------|-------------|
| Strategy A — Raw Retrieval     |      3          |        4        |     0.75    |
| Strategy B — Enhanced Retrieval|      4          |        4        |     1.00    |

## Observation

Strategy A retrieved broad AWS-related chunks, including partially irrelevant role-oriented content.

Strategy B produced more semantically focused cloud-computing and infrastructure-related retrievals after query enhancement.

The enhanced query improved:
- semantic specificity
- cloud computing alignment
- infrastructure relevance

while reducing retrieval noise.

---

## Query 2

### Original Query
What is aws vpc?

### Enhanced Query
What is Amazon Web Service Virtual Private cloud?

---

## Strategy A — Raw Retrieval

| Rank | Page | Chunk Summary                                                | Relevance  |
|------|------|--------------------------------------------------------------|------------|
| 1    | 15   | VPC networking, subnets, gateways, and AWS Direct Connect    | High       |
| 2    | 15   | AWS networking introduction and Amazon VPC overview          | High       |
| 3    | 2    | AWS certification and career information                     | Low        |
| 4    | 2    | General AWS hosting and certification overview               | Medium     |

---

## Strategy B — Enhanced Retrieval

| Rank | Page | Chunk Summary                                                    | Relevance  |
|------|------|------------------------------------------------------------------|------------|
| 1    | 15   | Amazon VPC overview, networking, subnets, and EC2 resources      | High       |
| 2    | 0    | AWS cloud computing platform and cloud services                  | Medium     |
| 3    | 15   | VPC gateways and AWS Direct Connect networking                   | High       |
| 4    | 2    | AWS infrastructure and cloud computing introduction              | Medium     |

---


## Precision@4 Evaluation

|           Strategy             | Relevant Chunks | Total Retrieved | Precision@4 |
|--------------------------------|-----------------|-----------------|-------------|
| Strategy A — Raw Retrieval     |      3          |        4        |     0.75    |
| Strategy B — Enhanced Retrieval|      4          |        4        |     1.00    |


## Observation

Strategy A retrieved relevant VPC-related chunks but also included certification-oriented and general AWS content.

Strategy B produced more semantically focused networking and cloud infrastructure retrievals after query enhancement.

The enhanced query improved:
- VPC terminology alignment
- networking relevance
- cloud infrastructure specificity

while reducing unrelated retrieval noise.

---

## Query 3

### Original Query
aws iam

### Enhanced Query
Amazon Web Services Identity and access management(IAM)

---

## Strategy A — Raw Retrieval

| Rank | Page | Chunk Summary                                                  | Relevance  |
|------|------|----------------------------------------------------------------|------------|
| 1    | 20   | IAM users, policies, groups, and roles overview                | High       |
| 2    | 28   | AWS Solutions Architect and SysOps responsibilities            | Low        |
| 3    | 19   | AWS IAM security, permissions, and multi-factor authentication | High       |
| 4    | 1    | General AWS cloud computing and deployment services            | Medium     |

---

## Strategy B — Enhanced Retrieval

| Rank | Page | Chunk Summary                                                     | Relevance  |
|------|------|-------------------------------------------------------------------|------------|
| 1    | 19   | AWS IAM security, permissions, and multi-factor authentication    | High       |
| 2    | 20   | IAM users, policies, groups, and roles overview                   | High       |
| 3    | 20   | IAM role permissions and temporary security credentials           | High       |
| 4    | 0    | AWS cloud security and storage services                           | Medium     |

---


## Precision@4 Evaluation

|           Strategy             | Relevant Chunks | Total Retrieved | Precision@4 |
|--------------------------------|-----------------|-----------------|-------------|
| Strategy A — Raw Retrieval     |      3          |        4        |     0.75    |
| Strategy B — Enhanced Retrieval|      4          |        4        |     1.00    |



## Observation

Strategy A retrieved relevant IAM-related chunks but also included broader AWS infrastructure and career-oriented content.

Strategy B produced more semantically focused security and identity-management retrievals after query enhancement.

The enhanced query improved:
- IAM terminology alignment
- security and access-management relevance
- authentication and permissions context

while reducing unrelated infrastructure-oriented retrieval noise.


## Overall Observation

Across all benchmark queries, the AI-enhanced retrieval strategy consistently achieved higher Precision@4 scores compared to raw vector similarity search.

Semantic query expansion improved:
- terminology alignment
- contextual relevance
- retrieval specificity

while reducing unrelated retrieval noise.