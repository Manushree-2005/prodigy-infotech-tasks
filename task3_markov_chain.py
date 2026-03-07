{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPww9WsfPD+b6Vx+cKj2Hr+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Manushree-2005/prodigy-infotech-tasks/blob/main/task3_markov_chain.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YLF4z9sgnAHN",
        "outputId": "d2488392-cd3c-4966-9ce8-81fb2ab7f284"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting markovify\n",
            "  Downloading markovify-0.9.4-py3-none-any.whl.metadata (23 kB)\n",
            "Collecting unidecode (from markovify)\n",
            "  Downloading Unidecode-1.4.0-py3-none-any.whl.metadata (13 kB)\n",
            "Downloading markovify-0.9.4-py3-none-any.whl (19 kB)\n",
            "Downloading Unidecode-1.4.0-py3-none-any.whl (235 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m235.8/235.8 kB\u001b[0m \u001b[31m9.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: unidecode, markovify\n",
            "Successfully installed markovify-0.9.4 unidecode-1.4.0\n"
          ]
        }
      ],
      "source": [
        "!pip install markovify"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import markovify\n",
        "\n",
        "text = \"\"\"\n",
        "Artificial intelligence is transforming industries across the world.\n",
        "Machine learning allows computers to learn patterns from data.\n",
        "Deep learning models can analyze complex information.\n",
        "Natural language processing helps machines understand human language.\n",
        "AI is widely used in healthcare, finance, and automation.\n",
        "Generative AI systems can create text, images, and music.\n",
        "Data science combines statistics, programming, and machine learning.\n",
        "Artificial intelligence will continue to shape the future of technology.\n",
        "AI models are improving search engines and recommendation systems.\n",
        "Robotics and AI are working together in modern manufacturing.\n",
        "\"\"\"\n",
        "\n",
        "model = markovify.Text(text, state_size=1)\n",
        "\n",
        "for i in range(5):\n",
        "    print(model.make_sentence())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lkQO4ZbtnLa0",
        "outputId": "d59b25b6-f06a-4a5c-a43b-53244d1373d9"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Deep learning allows computers to shape the future of technology.\n",
            "Data science combines statistics, programming, and recommendation systems.\n",
            "Robotics and recommendation systems.\n",
            "Artificial intelligence is widely used in modern manufacturing.\n",
            "Deep learning allows computers to shape the world.\n"
          ]
        }
      ]
    }
  ]
}