The most useful layouts for the purpose of this application are:
  - ForceAtlas
  - YifanHu
  - NoOverlap and Label Adject

1.Firsty its undordered
2.Use **force atlas** at repulsion strength = 5000. This will separate the two networks belonging to AB and MS respectively. The repulsion strength can be changed dynamically to suit the needs of the user. Feel free to use other convenient values like 500, 1000, or 10000.
3.Use statistics - **modularity**. For starters, accept all default settings. Later on, on left side task bar, node colours(and hence edges too) can be grouped depending on this attribute.
4.Use **NoOverlap** and **LabelAdjust** to view graph nodes properly
5.Use **YifanHu** to clean up and straighten the curved nature of the graphs. This helps in getting a much cleaner look to the networks, hence the zoomed-in versions can be better understood. However, it is important to note that this layout is better effective if used **after** using the ForceAtlas layout operation, not before.
